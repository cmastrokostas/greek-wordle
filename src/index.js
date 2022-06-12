import React, {useEffect} from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import wordList from "./el_GR_n_5.txt" ; 
import {genWordSet} from "./Words.js";

let request = new XMLHttpRequest();
request.open('GET', 'http://localhost:8080/dailyword')
request.send();
request.onload = () => {
    console.log(request.responseText)
}

const dailyWord = request.responseText
var disabled_letters = []

function Letter(props, i) {

    let sqStyle= "";
    if(props.class==="almost"){

        sqStyle={animation:"flip 0.7s ease forwards",backgroundColor: "#c5af41",};
    }
    else if(props.class==="correct"){
        sqStyle={animation:"flip 0.7s ease forwards",backgroundColor: "#458a40",};
    }
    else if (props.class === "false"){
        sqStyle={animation:"flip 0.7s ease forwards",backgroundColor: "#f8f8f8",};
    }
    else{
        sqStyle={backgroundColor: "#f8f8f8",};

    }
    
    return(
        <button className= "square" style = {sqStyle}>
            {props.content}
        </button>
    );
}


class Word extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
        }
    }

    renderLetter(i) {
        //const colours = ["correct", "correct", "false", "false", "false"];

        return(
            <Letter content = {this.props.content[i]} class = {this.props.colours[i]}/>
        );
    }

    render() {
        return (
            <div className='board-row'>
                {this.renderLetter(0)}
                {this.renderLetter(1)}
                {this.renderLetter(2)}
                {this.renderLetter(3)}
                {this.renderLetter(4)}
            </div>
        )
        
    }
}


function Key(props) {
    let sqStyle= {};
    if(disabled_letters.includes(props.value)){
        sqStyle = {backgroundColor: "#626262"}
    }
    else{sqStyle = {backgroundColor: "#f8f8f8"};
    }
    return (
        <button className="key-button" onClick={props.onClick} style = {sqStyle}>
            {props.value}
        </button>
    )
}

class Keyboard extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
        }

    }



    renderKey(i) {
        return(
            <Key value = {i}
                onClick={() => this.handleClick(i)}
            />
        )
    }

    handleClick(i) {
        this.props.callback(i);
    }

    

    render() {
        return(
            <div className='keyboard'>
                <div className = 'key-row'>
                    {this.renderKey('Ε')}
                    {this.renderKey('Ρ')}
                    {this.renderKey('Τ')}
                    {this.renderKey('Υ')}
                    {this.renderKey('Θ')}
                    {this.renderKey('Ι')}
                    {this.renderKey('Ο')}
                    {this.renderKey('Π')}
                </div>
                <div className = 'key-row'>
                    {this.renderKey('Α')}
                    {this.renderKey('Σ')}
                    {this.renderKey('Δ')}
                    {this.renderKey('Φ')}
                    {this.renderKey('Γ')}
                    {this.renderKey('Η')}
                    {this.renderKey('Ξ')}
                    {this.renderKey('Κ')}
                    {this.renderKey('Λ')}
                </div>
                <div className = 'key-row'>
                    {this.renderKey('Enter')}
                    {this.renderKey('Ζ')}
                    {this.renderKey('Χ')}
                    {this.renderKey('Ψ')}
                    {this.renderKey('Ω')}
                    {this.renderKey('Β')}
                    {this.renderKey('Ν')}
                    {this.renderKey('Μ')}
                    {this.renderKey('Del')}
                </div>
            </div>
        )
    }

    
}

class Board extends React.Component {
    constructor(props) {
        super(props);
        const words = Array(6).fill();
        const colours = Array(6).fill()
        const dailyWord = 'ΣΩΣΤΟ'

        const wordSet = genWordSet();
        for(let i=0;i<words.length;i++){
            words[i] = Array(5).fill(null)
            colours[i]=Array(5).fill("square");
        }
        this.state = {
            words: words,
            colours: colours,
            tries: 0,
            wordSet: wordSet,
            dailyword: 'ΣΩΣΤΟ',
        };

        this.callbackLetterClicked=this.callbackLetterClicked.bind(this);
    }

    callbackLetterClicked (letter) {

        const words = this.state.words.slice() //copy cause we want immutability
        const colours= this.state.colours.slice()
        //increases index until it finds the first non-null item
        let ind1 = this.state.tries;
        let ind2 = 0;

        while(words[ind1][ind2]){
            ind2++;
        } 

        if(letter === 'Del'){
            words[ind1][ind2-1] = null;
            ind2--;
        } else if(letter === 'Enter') {
            let flag = false;
            if(ind2 === 5){
                let currWord='';
                for(let i=0;i<5;i++){
                    currWord+=this.state.words[ind1][i];
                }
                if(currWord === this.state.dailyword){
                    this.setState({tries: -1});
                    alert("Σωστή Λέξη!") // finish game 
                    //todo Return Session Stats
                }
                else if(this.state.wordSet.has(currWord)){
                    console.log('eureka');
                    this.setState({tries: ind1+1});
                }
                else{
                    flag=true;
                    alert("Μη Έγκυρη Λεξη!")
                }
            }
            //elgxos gia xrwma

            if(!flag && ind2 === 5){
                colours[ind1]  = checkColours(words[ind1], colours[ind1], this.state.dailyword);
            }
        } else if(ind2 <= 4){
            words[ind1][ind2] = letter;
        }
        this.setState({
            words: words,
            colours: colours,
        })
    }

    renderWord(i) {
        return(
            <Word content = {this.state.words[i]} colours = {this.state.colours[i]}/>
        )
    }

    render() {
        return (
            <div className='game-board'>
                <div className = 'words'>
                    {this.renderWord(0)}
                    {this.renderWord(1)}
                    {this.renderWord(2)}
                    {this.renderWord(3)}
                    {this.renderWord(4)}
                    {this.renderWord(5)}
                </div>
                <div className='keyboard'>
                    <Keyboard callback = {this.callbackLetterClicked}/>
                </div>
            </div>
        )
    }
}
class Game extends React.Component {

    render() {
        return (
            <div className = "game">
                <nav >
                    <h1 className = "title">Greekλe</h1>
                </nav>
                <Board/>
            </div>
        );
    }
    
}

function checkColours(word, colours, dailyWord) {
    //word[.....], colours=[.....], dailyword
    for(let i=0;i<5;i++){
        if (dailyWord[i] === word[i]){
            colours[i] = 'correct'
        }
        else if (word[i] !== "" && dailyWord.includes(word[i])){
            colours[i] = 'almost'
        }
        else{
            colours[i] = 'false'
            disabled_letters.push(word[i]);
        }
    }
    return colours;
}

const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(<Game />);