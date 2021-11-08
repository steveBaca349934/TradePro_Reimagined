
import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";

export default class App extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <HomePage />
      </div>
    );
  }
}


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


const appDiv = document.getElementById("app");
render(<App />, appDiv);