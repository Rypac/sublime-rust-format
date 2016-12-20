# RustFormat

A simple plugin to format Rust code.

## Commands

- `RustFormat: Format Selection`
    + Format the current selection
- `RustFormat: Format File` (<kbd>Ctrl+k</kbd>, <kbd>Ctrl+f</kbd>)
    + Format the current file
- `RustFormat: Enable Format on Save`
    + Enable automatic formatting of Rust source files on save
- `RustFormat: Disable Format on Save`
    + Disable automatic formatting of Rust source files on save

## Configuration

- `rust_format_on_save`
    + Automatically format files on save
- `rust_format_binary`
    + Full path to `rustfmt` binary (if not on `PATH`)
