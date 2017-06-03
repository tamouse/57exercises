import React, {Component} from 'react';
import {BrowserRouter as Router, Route, Link} from 'react-router-dom';
import logo from './logo.svg';
import './App.css';
import Home from './exercises/home';

const routes = [
    {path: '/', exact: true, linkText: 'Home', sidebar: () => <div>Home</div>, main: Home}
];

const SideBar = () => (
    <div className="App--Sidebar">
        <header>
            <img className="App-logo" src={ logo } alt="React.JS Logo"/>
            <h2>
                React.JS version of Brian P. Hogan's 57 Exercises for Programmers
            </h2>
        </header>
        <ul>
            {routes.map((route, index) => (
                <li key={index}>
                    <Link to={route.path}>{route.linkText}</Link>
                </li>
            ))}
        </ul>
    </div>
);

const Main = () => (
    <div className="App--Main">
        {routes.map((route, index) => (
            <Route
                key={index}
                path={route.path}
                exact={route.exact}
                component={route.main}
            />
        ))}
    </div>
);

class App extends Component {
    render() {
        return (
            <Router>
                <div className="flex-to-fill-height">
                    <div className="flex-child-to-fill-height">
                        <div className="App">
                            <SideBar/>
                            <Main/>
                        </div>
                    </div>
                </div>
            </Router>
        );
    }
}

export default App;

