# The adventure app

## Not comfortable with Flet yet? Start here!

If you're not comfortable working with Flet yet, it's a good idea to build your adventure world first.

**Don't start Flet just yet.** Instead, navigate to the `src` folder and run `show.py` (**not `main.py`**).

Play through the adventure and try all the available choices. Then explore the code to understand how the different files work together:

- Where is the player created?
- How does the shop work?
- Where do the messages displayed to the player come from?
- How do the different files communicate with each other?

Once you understand the structure, continue developing your adventure based on your sketches and plans in Google Classroom.

Later, you'll replace `show.py` with interactive Flet scenes. The `while` loop will be replaced by button interactions, `input()` by text input fields, `print()` by Flet text controls, and so on.

**Before your start changing to Flet, your adventure must contain AT LEAST five functional scenes:** the village, the shop, the bridge, the forest, and the ruins (or similar locations that fit your own story).

Remember: the example code is just a starting point. You are responsible for developing the story, implementing the choices, and deciding what happens in each scene. And to go from CLI to a nice looking story implemented with flet!

## Run the app

### uv

Run as a desktop app:

```bash
uv run flet run
```

Run as a web app:

```bash
uv run flet run --web
```

For more details on running the app, refer to the [Getting Started Guide](https://flet.dev/docs/).

## Build the app

### Android

```bash
flet build apk -v
```

For more details on building and signing `.apk` or `.aab`, refer to the [Android Packaging Guide](https://flet.dev/docs/publish/android/).

### iOS

```bash
flet build ipa -v
```

For more details on building and signing `.ipa`, refer to the [iOS Packaging Guide](https://flet.dev/docs/publish/ios/).

### macOS

```bash
flet build macos -v
```

For more details on building macOS package, refer to the [macOS Packaging Guide](https://flet.dev/docs/publish/macos/).

### Linux

```bash
flet build linux -v
```

For more details on building Linux package, refer to the [Linux Packaging Guide](https://flet.dev/docs/publish/linux/).

### Windows

```bash
flet build windows -v
```

For more details on building Windows package, refer to the [Windows Packaging Guide](https://flet.dev/docs/publish/windows/).

### Web

```bash
flet build web -v
```

For more details on building Web app, refer to the [Web Packaging Guide](https://flet.dev/docs/publish/web/).
