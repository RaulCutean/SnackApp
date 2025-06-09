import React from 'react';
import hourglass from '../../assets/hourglass.svg'

const DurationBadge = ({duration}) => {
    return (
        <div className="recipe-duration">
            <img src={`${hourglass}`} alt="#"/>
            {duration}
        </div>
    );
};

export default DurationBadge;