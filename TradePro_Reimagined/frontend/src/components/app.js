import React, { Component } from "react";
import { render } from "react-dom";
import HomePage from "./HomePage";



/**
 * Note -> we need "export" in order to export a class to another file...
 * Similar to __init__.py in python
 */

export default class App extends Component{

    constructor(props){
        /*
        a prop is an 'element' of sorts that we pass
        to the component, that the component can then utilize
        */
        super(props);
    }

    render(){

        /**
         * whenever we utilize the square brackets {}
         * this allows us to insert javascript into our html text
         */
        return (<div>
            <HomePage />
     
            </div>
            );
    }

}


const appDiv = document.getElementById("app");
/*this takes the "render()" function we declared above 
and inserts this into the appDiv from index.html
*/
render(<App name="Steve" />, appDiv);