import sublime
import sublime_plugin
import subprocess
import os


def is_rust(view):
    return view.score_selector(0, 'source.rust') > 0


def is_windows():
    return os.name == 'nt'


def settings():
    return sublime.load_settings('RustFormat.sublime-settings')


class RustFormatCommand(sublime_plugin.TextCommand):
    def is_enabled(self):
        return is_rust(self.view)

    def run(self, edit):
        startupinfo = None
        if is_windows():
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE

        binary = settings().get('rust_format_binary') or 'rustfmt'
        rustfmt = subprocess.Popen(
            [binary, '--write-mode=overwrite', self.view.file_name()],
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            startupinfo=startupinfo,
            universal_newlines=True)

        output, error = rustfmt.communicate()
        if error:
            print('RustFormat:', error)


class RustFormatListener(sublime_plugin.EventListener):
    def on_post_save_async(self, view):
        if is_rust(view) and settings().get('rust_format_on_save', False):
            view.run_command('rust_format')
