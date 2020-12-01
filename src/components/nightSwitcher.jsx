import React, { Component } from "react";
import ReactDOM from "react-dom";

class NightSwitcher extends Component {
  constructor() {
    super();

    this.state = {
      night: false,
    };

    this.handleClick = this.handleClick.bind(this);
  }

  handleClick(event) {
    this.setState(() => {
      return {
        night: !this.state.night,
      };
    });
  }

  render() {
    return <button onClick={this.handleClick}></button>;
  }
}

const domContainer = document.querySelector("#night-switcher");
ReactDOM.render(React.createElement(NightSwitcher), domContainer);
