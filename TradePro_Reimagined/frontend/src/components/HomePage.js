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

/**
 * so these are the classes we 
 * are returning from the ImplementHomePage Render() function
 * kinda stupid that Im mixing OOP and Functional Programming
 * Will clean up later
 */
 let intro = document.querySelector(".intro")
 let lego = document.querySelector(".logo-header")
 let logoSpan = document.querySelector(".logo")
 

/**
 * good ole lambda function which triggers on webpage loading
 */
window.addEventListener("DOMContentLoaded", () => {

  setTimeout(() => {
    logoSpan.forEach((span, idx) => {
      setTimeout(() => {

        span.classList.add("active");

      }, (idx + 1) * 400)

    });

    setTimeout(() => {
      logoSpan.forEach((span, idx) => {

        setTimeout(() => {


          span.classList.remove("active");
          span.classList.add("fade");


        }, (idx + 1) * 50)

      })

    }, 2000);

    setTimeout(() => {
      intro.style.top = '-100vh';


    }, 2300)

  })

})



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
