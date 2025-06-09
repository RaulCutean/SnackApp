import React, {useEffect, useState} from 'react';
import {FormControl, FormGroup, Modal} from 'react-bootstrap';
import './AddCategoryModal.css'
import Form from "react-bootstrap/Form";

const AddCategoryModal = (props) => {
    const [name, setName] = useState('')
    const [color, setColor] = useState('')
    const saveCategory = async (event) => {
        event.preventDefault()
        const data = {
            name , color
        }
        const responseObject = await fetch(`${import.meta.env.VITE_API_URL}/categories` , {
            method: 'POST' ,
            headers: {
                'Content-Type': 'application/json'
            },
            body : JSON.stringify(data)
        })
        setName('')
        setColor('')
        props.handleClose()
    }
    return (
        <Modal show={props.show}  onHide={props.handleClose}>
            <Modal.Header closeButton>
                <Modal.Title>Add Category</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Form >
                    <FormGroup>
                        <Form.Label>Category name</Form.Label>
                        <FormControl
                            placeholder={"Enter a category name"}
                            value={name}
                            onChange={(e) => setName(e.target.value)}
                        />
                    </FormGroup>
                    <FormGroup>
                        <Form.Label>Category color</Form.Label>
                        <FormControl
                            type={"color"}
                            value={color}
                            onChange={(e) => setColor(e.target.value)}/>
                    </FormGroup>
                    <button onClick={saveCategory}>Add category</button>
                </Form>
            </Modal.Body>
        </Modal>
    );
};

export default AddCategoryModal;