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


def save_settings():
    return sublime.save_settings('RustFormat.sublime-settings')


def process_startup_info():
    if not is_windows():
        return None
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = subprocess.SW_HIDE
    return startupinfo


def rustfmt(args=[], input=None):
    binary = settings().get('rust_format_binary') or 'rustfmt'
    return subprocess.Popen(
        [binary] + args,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        startupinfo=process_startup_info(),
        universal_newlines=True).communicate(input=input)


def print_error(error):
    print('RustFormat:', error)


class RustFormatSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if region.empty():
                continue

            selection = self.view.substr(region)
            output, error = rustfmt(input=selection)
            if not error:
                self.view.replace(edit, region, output)
            else:
                print_error(error)


class RustFormatFileCommand(sublime_plugin.TextCommand):
    def is_enabled(self):
        return is_rust(self.view)

    def run(self, edit):
        args = ['--emit=files', self.view.file_name()]
        output, error = rustfmt(args)
        if error:
            print_error(error)


class RustFormatListener(sublime_plugin.EventListener):
    def on_post_save_async(self, view):
        if is_rust(view) and settings().get('rust_format_on_save'):
            view.run_command('rust_format_file')


class RustFormatToggleOnSaveCommand(sublime_plugin.ApplicationCommand):
    def is_checked(self):
        return settings().get('rust_format_on_save')

    def run(self):
        format_on_save = settings().get('rust_format_on_save')
        settings().set('rust_format_on_save', not format_on_save)
        save_settings()


class RustFormatEnableOnSaveCommand(RustFormatToggleOnSaveCommand):
    def is_visible(self):
        return not settings().get('rust_format_on_save')


class RustFormatDisableOnSaveCommand(RustFormatToggleOnSaveCommand):
    def is_visible(self):
        return settings().get('rust_format_on_save')
