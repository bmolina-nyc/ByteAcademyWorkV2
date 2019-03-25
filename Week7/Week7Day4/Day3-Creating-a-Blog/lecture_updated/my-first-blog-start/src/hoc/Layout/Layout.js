import React from 'react';

import Aux from '../../hoc/Auxilary/Aux';
import './Layout.css';
import Toolbar from '../../components/ToolBar/ToolBar'


const layout = (props ) => (
    <Aux>
        <Toolbar />
        <main className="Content">
          {props.children}
        </main>
    </Aux>
)

export default layout;