import sublime_plugin
import subprocess


def is_rust(view):
    return "source.rust" in view.scope_name(0)


class RustFormatCommand(sublime_plugin.TextCommand):

    def is_enabled(self):
        return is_rust(self.view)

    def run(self, edit):
        rustfmt = subprocess.Popen(
            ['rustfmt', self.view.file_name()],
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
            shell=True)
        output, errors = rustfmt.communicate()
        if self.view.settings().get('rust_format_debug', False):
            print(
                'RustFormat: ', str(output.strip()), '\n',
                'Errors:', str(errors.strip()))


class RustFormatListener(sublime_plugin.EventListener):

    def on_post_save_async(self, view):
        if is_rust(view) and view.settings().get('rust_format_on_save', False):
            view.run_command('rust_format')
