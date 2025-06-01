import React from 'react';
import { Outlet } from "react-router";
import {Navbar} from "../Navbar/Navbar.jsx";

const LayoutOutlet = () => {
    return (
        <div>
            <Navbar />
            <Outlet />
        </div>
    );
};

export default LayoutOutlet;