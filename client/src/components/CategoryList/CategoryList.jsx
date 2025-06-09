import React from 'react';
import './CategoryList.css'

const CategoryList = ({categories}) => {
    return (
        <div className="recipe-categories">
            {categories.map((category) => {
                return (
                    <div
                        className={"category-badge"}
                        style={{backgroundColor: category.color}}
                        key={`${category.id}`}
                    >
                        {category.name}
                    </div>
                )
            })}
        </div>
    );
};

export default CategoryList;