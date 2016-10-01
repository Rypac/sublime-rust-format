# RustFormat

A simple plugin to format Rust code.

## Prerequisites

This package relies on the amazing [rustfmt](https://github.com/rust-lang-nursery/rustfmt) to format Rust source code files.

Install using `cargo install rustfmt` or via instructions on the [website](https://github.com/rust-lang-nursery/rustfmt#installation).

## Installation

1. Install Package Control
2. Run `Package Control: Install Package` in the Command Palette (<kbd>Super+Shift+P</kbd>)
3. Install `RustFormat`

## Usage

Run the `RustFormat: Format File` command to format the current file.

Alternatively the command can be invoked using the default keyboard shortcut (<kbd>Ctrl+k</kbd>, <kbd>Ctrl+f</kbd>).

## Configuration

- `rust_format_on_save`
    + Automatically format files on save
- `rust_format_binary`
    + Full path to `rustfmt` binary (if not on `PATH`)
