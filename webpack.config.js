const path = require("path");
const webpack = require("webpack");
//css modules and css dumping
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
//css minification
const TerserPlugin = require("terser-webpack-plugin");

module.exports = {
  mode: "development",

  entry: {
    components: [
      "./src/components/nightSwitcher.jsx",
      "./src/components/myButton.jsx",
    ],
    style: "./src/style/main.scss",
  },

  output: {
    path: path.resolve(__dirname, "src/opale/static"),
  },

  plugins: [new webpack.ProgressPlugin(), new MiniCssExtractPlugin()],

  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: {
            presets: [
              //["es2015", { modules: false }], // IMPORTANT
            ],
          },
        },
      },
      {
        test: /.(scss|css)$/,

        use: [
          {
            loader: MiniCssExtractPlugin.loader,
          },
          {
            loader: "css-loader",

            options: {
              sourceMap: true,
            },
          },
          {
            loader: "sass-loader",

            options: {
              sourceMap: true,
            },
          },
        ],
      },
    ],
  },

  optimization: {
    minimizer: [new TerserPlugin()],
  },
};
