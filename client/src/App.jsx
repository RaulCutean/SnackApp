import {useEffect, useState} from 'react'
import './App.css'
import { BrowserRouter, Route , Routes} from "react-router";
import HomePage from "./components/pages/HomePage.jsx";
import {Navbar} from "./components/Navbar/Navbar.jsx";
import "./components/Navbar/Navbar.jsx"
import LayoutOutlet from "./components/Layout/LayoutOutlet.jsx";
import RecipeContextProvider from "./components/Context/RecipeContextProvider.jsx";

function App() {


  return (
    <>
        {/*<Navbar />*/}
        <BrowserRouter>
            <RecipeContextProvider>
                <Routes>
                    <Route path='/' element={<LayoutOutlet />}>
                        <Route index element = {<HomePage />}/>
                    </Route>
                </Routes>
            </RecipeContextProvider>
        </BrowserRouter>
    </>
  )
}

export default App
