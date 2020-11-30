const path = require("path");
const webpack = require("webpack");
//css modules and css dumping
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
//css minification
const TerserPlugin = require("terser-webpack-plugin");

module.exports = {
  mode: "development",

  entry: {
    nightSwitcher: "./src/components/nightSwitcher.jsx",
    //componentTwo: "./src/components/componentTwo.js",
    opale_extra: "./src/style/main.scss",
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
