# Sit Down Please

[日本語](./README.md)

![](./sit-down-please.webp)

IoT software for sit rental services, like library and net cafe.

## Technologies

- Nuxt.js
- Flask
- Raspberry Pi

## Features

- Displays the current time
- Indicates whether the user is sitting or not
- Shows the duration of time the user has been seated

## Demonstrations

![iPhone Mockup](mockup_iphone.jpg)
![iPad Mockup](mockup_ipad.jpg)
![MacBook Pro Mockup](mockup_macbook.jpg)

## Usage

### Installation

Clone from GitHub to install

```sh
git clone https://github.com/KleinChiu/sit-down-please.git
```

Alternatively, you can download zip from GitHub and decompress it.
But it will cause you harder to update.

Install dependencies

```sh
sh install.sh
```

### Execution

```sh
pm2 start ecosystem.config.json
```

## Note

This is an IoT project that is connected to a Raspberry pi.

## Contribution

If you want to contribute to the project, please feel free to submit a pull request.

## License

This project is licensed under the MIT License.

![](sit-down-please.webp)
