import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';
import Prompts from './Prompts';
import Madlib from './Madlib';

class App extends Component {
    render() {
        return (
            <div className="App">
                <div className="App-header">
                    <img src={logo} className="App-logo" alt="logo"/>
                    <h2>MadLibs</h2>
                </div>
                <p className="App-intro">
                    From Bryan Hogan's <em>Exercises for Programmers</em>.
                    Built with create-react-app.
                </p>
                <Prompts/>
                <Madlib/>
            </div>
        );
    }
}

export default App;
