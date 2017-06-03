import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h2>Brian P. Hogan's 57 Exercises for Programmers implemented in React.JS</h2>
          <h3><a href="https://github.com/tamouse" target="_blank" title="Github Repo" rel="noopener noreferrer">Implemented by Tamara Temple </a></h3>
        </div>
      </div>
    );
  }
}

export default App;
