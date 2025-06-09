import React from 'react';
import { Outlet } from "react-router";
import {Navbar} from "../Navbar/Navbar.jsx";

const LayoutOutlet = (props) => {
    return (
        <div>
            <Navbar handleOpenCategoryModal={props.handleOpenCategoryModal}
                    handleOpenRecipeModal={props.handleOpenRecipeModal}
            />
            <Outlet />
        </div>
    );
};

export default LayoutOutlet;