import React from 'react';
import './Navbar.css'

export function Navbar({handleOpenCategoryModal , handleOpenRecipeModal}) {
    return (
        <nav>
            <div className="logo">
                FullSnack
            </div>
            <div style ={
                {
                    display: "flex",
                    gap: "0.5rem" ,
                }
            }>
                <button onClick={handleOpenCategoryModal}>
                    + Add category
                </button>
                <button onClick={handleOpenRecipeModal}>
                    + Add recipe
                </button>
            </div>
        </nav>
    );
}
