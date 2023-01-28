import React, { Component } from "react";

class TextFields extends Component {
  state = {
    error: false,
  };
  render() {
    return (
      <div>
        <textarea
          error={this.state.error}
          id="standard-error-helper-text"
          label="Upper Number"
          type="number"
          variant="outlined"
        />
      </div>
    );
  }
}

export default TextFields;
