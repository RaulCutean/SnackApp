import {useEffect, useState} from 'react'
import './App.css'
import { BrowserRouter, Route , Routes} from "react-router";
import HomePage from "./components/pages/HomePage.jsx";
import {Navbar} from "./components/Navbar/Navbar.jsx";
import "./components/Navbar/Navbar.jsx"
import LayoutOutlet from "./components/Layout/LayoutOutlet.jsx";
import RecipeContextProvider from "./components/Context/RecipeContextProvider.jsx";
import AddCategoryModal from "./components/Modal/AddCategoryModal.jsx";
import AddRecipeModal from "./components/Modal/AddRecipeModal.jsx";
import RecipeDetails from "./components/pages/RecipeDetails.jsx";

function App() {
  const [showCategoryModal, setShowCategoryModal] = useState(false);
  const [showRecipeModal, setShowRecipeModal] = useState(false)
  return (
    <>
        {/*<Navbar />*/}
        <BrowserRouter>
            {/*<RecipeContextProvider>*/}
                <Routes>
                    <Route path='/' element={<LayoutOutlet
                        handleOpenCategoryModal = {() => setShowCategoryModal(true)}
                        handleOpenRecipeModal = {() => setShowRecipeModal(true)}
                    />}
                    >
                        <Route index element = {<HomePage />}/>
                        <Route path={'/recipe/:id'} element = {<RecipeDetails />}/>
                    </Route>
                </Routes>
            {/*</RecipeContextProvider>*/}
        </BrowserRouter>
        <AddCategoryModal show ={showCategoryModal} handleClose={() => setShowCategoryModal(false)} />
        <AddRecipeModal show={showRecipeModal} handleClose={() => setShowRecipeModal(false)}/>
    </>
  )
}

export default App
