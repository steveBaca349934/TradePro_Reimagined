import React, { Component } from "react";
import CreateRAT from "./CreateRAT";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";


class ImplementHomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {

    return (

      <p>We are implementing the home page</p>
      
    );


  }
}

export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/" component={ImplementHomePage} />
          <Route path="/RAT" component={CreateRAT} />
        </Switch>
      </Router>
    );
  }
}
