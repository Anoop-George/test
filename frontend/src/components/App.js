import React, { Component } from "react";
import { render } from "react-dom";
import PersistentDrawerLeft from './drawer'

class App extends Component {
  
  render() {
    return (
      <div>
        <PersistentDrawerLeft/>
        
      </div>
    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);