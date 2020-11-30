import React, { Component } from "react";
import ReactDOM from "react-dom";

class NightSwitcher extends Component {
  constructor() {
    super();

    this.state = {
      night: false,
    };

    this.handleChange = this.handleChange.bind(this);
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
