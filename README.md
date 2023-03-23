# DASH VanArt Lite
Welcome to DASH VanArt Lite.

## Introduction

Public art is an important aspect of any city as it reflects the culture, history, and values of a community. Vancouver is known for its vibrant and diverse arts scene, and as a result, it has a plethora of public art installations that locals and tourists can explore. However, apart from some well-known museums that gather art collections together, with so many public art installations scattered throughout the city, it can be difficult for tourists to find the art they are interested in. As a result, we want to provide tourists with a centralized location to find information on public art in Vancouver.

Link to the original [proposal] (https://github.com/UBC-MDS/VanArt/blob/main/reports/proposal.md)
## Usage

Try out the app [here](https://dash-vanart-lite.onrender.com/).

Here are some general instructions on how to use the application:
(1) When you first view the application, you will notice that the main plot and table are already populated. Options have been selected for you in the `Select an Art Type` and `Select a Neighbourhood` field. This is to assist you with viewing how the application will function. 

(2) Review the header for more information about the application.

(3) Then navigate to the `Select an Art Type` drop down list and select all the options you'd like to include for Art Type. You can select as many options as you'd like. This will automatically update the graph and the table. 

(3) Next in the same row you can also navigate to the dropdown bar on the right titled `Select a Neighbourhood`. Once your preferred options are selected, you can see once again that both the graph and table will get updated. 

Enjoy experimenting with all the combinations of art types and neighbourhoods you want!

## Installation and run locally

To make this app run locally on your computer, please:

1. Clone or fork this repository first to your local directory.
2. Install the environment by following the installation instructions below. Then activate it.

```{bash}
conda env create --file vanart_env.yaml
conda activate vanart-lite
```

3. After installing the environment, navigate to the `src` directory of the repository on your computer and run the following command in the terminal:

```{bash}
python app.py
```

## Contributing

Interested in contributing? You are welcome to make contributions on our VanArt App!

Please check out the [contributing](CONTRIBUTING.md) guidelines. Please note that this project is released with a [Code of Conduct](CODE_OF_CONDUCT.md). By contributing to this project, you agree to abide by its terms.

## License

`DASH_VanArt_Lite` is licensed under the terms of the [MIT](LICENSE) license.