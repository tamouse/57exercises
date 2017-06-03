// The Home component, renders when the Home route is rendered

import React, { Component } from 'react';

class Home extends Component {
    render() {
        return (
            <div className="Home">
                <p>
                    Working through Brian Hogan's
                    <em>Exercises for Programmers: 57
                        Challenges to Develop Your Coding Skills</em>
                </p>
                <h3>React Branch</h3>
                <p>
                    For the React branch, I'm creating a react app in
                    <code>./57exercises/</code>
                    and
                    shifting all the exercises into components under
                    <code>./57exercises/src/exercises/...</code>.
                    The main app will be
                    pretty much just a big router as I work through the exercises.
                </p>
                <h3>Wheeee!</h3>
            </div>
        )
    }
}

export default Home;