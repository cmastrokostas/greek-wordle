import React, {useEffect} from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import wordList from "./el_GR_n_5.txt" ; 
import {genWordSet} from "./Words.js";

function Letter(props) {

    return(
        <button className='square'>
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
        return(
            <Letter content = {this.props.content[i]} />
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
    return (
        <button className="key-button" onClick={props.onClick} >
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
        const dailyWord = 'ΣΩΣΤΟ'

        const wordSet = genWordSet();
        for(let i=0;i<words.length;i++){
            words[i] = Array(5).fill(null)
        }
        this.state = {
            words: words,
            tries: 0,
            wordSet: wordSet,
            dailyword: 'ΣΩΣΤΟ'
        };

        this.callbackLetterClicked=this.callbackLetterClicked.bind(this);
    }
    
    callbackLetterClicked (letter) {

        const words = this.state.words.slice() //copy cause we want immutability
        //increases index until it finds the first non-null item
        let ind1 = this.state.tries;
        let ind2 = 0;

        while(words[ind1][ind2]){
            ind2++;
        } 

        if(letter === 'Del'){
            words[ind1][ind2-1] = null;
        } else if(letter === 'Enter') {

            if(ind2 === 5){
                let currWord='';
                for(let i=0;i<5;i++){
                    currWord+=this.state.words[ind1][i];
                }
                if(currWord === this.state.dailyword){
                    alert("Σωστή Λέξη!")
                    //todo Return Session Stats
                }
                else if(this.state.wordSet.has(currWord)){
                    console.log('eureka');
                    this.setState({tries: ind1+1});
                }
                else{
                    alert("Μη Έγκυρη Λεξη!")
                }
            }
        } else if(ind2 <= 4){
            words[ind1][ind2] = letter;
        }
        this.setState({
            words: words,
        })
    }

    renderWord(i) {
        return(
            <Word content = {this.state.words[i]}/>
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
                    <h1>Greek Wordle</h1>
                </nav>
                <Board/>
            </div>
        );
    }
    
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Game />);
