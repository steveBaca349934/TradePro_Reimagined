import React, { Component } from "react";
import CreateRAT from "./CreateRAT";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import TextField from "@material-ui/core/TextField";
import FormHelperText from "@material-ui/core/FormHelperText";
import FormControl from "@material-ui/core/FormControl";
import Radio from "@material-ui/core/Radio";
import RadioGroup from "@material-ui/core/RadioGroup";
import FormControlLabel from "@material-ui/core/FormControlLabel";


class ImplementHomePage extends Component {
  constructor(props) {
    super(props);
  }

  /**
   * Notes for myself about this render() function
   * <h1> div = the first header tag visible on a page
   * 
   * 
   */
  render() {

    return (

      <div class="intro">
        <h1 class ="logo-header">
          <span class ="logo">TradePro Reimagined</span>
        </h1>
      </div>

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
