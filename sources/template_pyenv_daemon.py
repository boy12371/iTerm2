#!/usr/bin/env python3.7

import iterm2
# To install packages from PyPI, use this command, changing package_name to the package you
# wish to install:
#   "$$PYTHON_BIN$$/pip3" install package_name

async def main(connection):
    # This is an example of a callback function. In this template, on_custom_esc is called when a
    # custom escape sequence is received. You can send a custom escape sequence with this command:
    #
    # printf "\033]1337;Custom=id=%s:%s\a" "shared-secret" "create-window"
    async def my_callback(match):
        await iterm2.Window.async_create(connection)

    # This code defines a custom control sequence and registers it.
    my_sequence = iterm2.CustomControlSequence(
        connection=connection,
        callback=my_callback,
        identity="shared-secret",
        regex=r'^create-window$')

    await my_sequence.async_register()

# This instructs the script to run the "main" coroutine and to keep running even after it returns.
iterm2.run_forever(main)
