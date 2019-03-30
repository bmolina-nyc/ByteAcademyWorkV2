import React, {Component} from 'react';
import NumberComponent from './Number'


class NumberButton extends Component{
    
    state = {
        showNumbers: false ,
        numbers: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    }

    showNumberHandler = () => {
     this.setState({showNumbers: !this.state.showNumbers})
    }

    render(){
        const numberComponents = this.state.numbers.map( (num, idx) =>
            <NumberComponent key={idx} num={num}  />
        )
    
        return(
            <div>
            <h1>Show Numbers</h1>
            <button onClick={this.showNumberHandler}>{this.state.showNumbers ? "Hide Numbers" : "Show Numbers" }</button>
            {this.state.showNumbers && numberComponents}
            </div>
        )
    }
}

export default NumberButton;
