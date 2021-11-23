import React, { Component } from "react";
import CreateRAT from "./CreateRAT";
import About from "./About";
import News from "./News";
import MeetTheTeam from "./MeetTheTeam"

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
import { Container } from "@material-ui/core";


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

        <div id="header">
          <h1 class="logo-header">
            <span class="logo">TradePro Reimagined</span>
          </h1>

          <h2>
            <form action="http://127.0.0.1:8000/RAT">
              <button id="intro-page-button">Take The Risk Assessment Test</button>
            </form>
          </h2>

          <h2>
            <form action="http://127.0.0.1:8000/About">
              <button id="intro-page-button-about">About</button>
            </form>
          </h2>

          <h2>
            <form action="http://127.0.0.1:8000/News">
              <button id="intro-page-button-news">News</button>
            </form>
          </h2>

          <h2>
            <form action="http://127.0.0.1:8000/MeetTheTeam">
              <button id="intro-page-button-meettheteam">Meet The Team</button>
            </form>
          </h2>
        </div>




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
          <Route path="/About" component={About} />
          <Route path="/News" component={News} />
          <Route path="/MeetTheTeam" component={MeetTheTeam} />
        </Switch>
      </Router>
    );
  }
}
