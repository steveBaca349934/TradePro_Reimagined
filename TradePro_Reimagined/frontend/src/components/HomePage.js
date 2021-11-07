import React, {Component} from "react";
import RoomJoinPage from "./RoomJoinPage";
import CreateRoomJoinPage from "./CreateRoomJoinPage";
import {BrowserRouter as Router, Switch, Route, Link, Redirect} from "react-router-dom";



export default class HomePage extends Component{
    constructor(props){
        super(props);
    }

    render(){
        return (
        <Router>     
            <Switch>
                <Route exact path = '/'><p>This is the homepage</p></Route>
                <Route path="/join" component={RoomJoinPage} />
                <Route path = '/create' component = {CreateRoomJoinPage} /> 
            </Switch>
        </Router>);
    }
}
