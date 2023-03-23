# DASH VanArt Lite
Welcome to DASH VanArt Lite!

## Introduction

Public art is an important aspect of any city as it reflects the culture, history, and values of a community. Vancouver is known for its vibrant and diverse arts scene, and as a result, it has a plethora of public art installations that locals and tourists can explore. However, apart from some well-known museums that gather art collections together, with so many public art installations scattered throughout the city, it can be difficult for tourists to find the art they are interested in. As a result, we want to provide tourists with a centralized location to find information on public art in Vancouver.

This dashboard is a lighter version of the original [VanArt RShiny](https://github.com/UBC-MDS/VanArt) app and the original proposal can be found [here](https://github.com/UBC-MDS/VanArt/blob/main/reports/proposal.md).

## Usage

To try out the app click [here](https://dash-vanart-lite.onrender.com/).

The application displays two main visualizations, a graph and a table. The graph is a stacked bar chart that shows you the number of art types per neighbourhood. While the table displays information on Art Name, Art Type, Neighbourhood, and Address. Both the graph and table will update based on your selection from the dropdown bars at the top. Review the sub-header at the top of the application for some general information about the application. 

Here are some general instructions on how to use the application:    
1. When you first view the application, you will notice that the main plot and table are already populated. Options have been selected for you in the `Select an Art Type` and `Select a Neighbourhood` dropdown fields. This is to assist you with viewing how the application will function.  

2. Then navigate to the `Select an Art Type` drop down list and select all the options you'd like to include for Art Type. You can select as many options as you'd like. This will automatically update the graph and the table. 

3. Next in the same row you can also navigate to the dropdown bar on the right titled `Select a Neighbourhood`. Once your preferred options are selected, you can see once again that both the graph and table will get updated. 

Enjoy experimenting with all the combinations of art types and neighbourhoods you want and see what types of public arts you can visit in Vancouver!

## To Install and Run Locally

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

## Data Used (Reference)

The data set we used to create this app is modified from [City of Vancouver Open Data Portal](https://opendata.vancouver.ca/explore/dataset/public-art/export/).

Our modified data contains the feature about: the title of the artwork, the type of art (mural, statue, etc.), address of artwork, neighborhood where the work is located, latitude and longitude of the artwork, the photo URL, URL with artwork information, brief introduction to the artwork, and the year artwork was installed.

## License

`DASH_VanArt_Lite` is licensed under the terms of the [MIT](LICENSE) license.
