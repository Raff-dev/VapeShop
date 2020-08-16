﻿import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { Grid, Glyphicon, Nav, Navbar, NavItem, Col } from 'react-bootstrap';
import { LinkContainer } from 'react-router-bootstrap';
import './NavMenu.css';

export const NavMenu = (props) => {

    return (
        <Navbar inverse fixedTop fluid collapseOnSelect>
            <Navbar.Header>
                <Navbar.Brand>
                    <Link to={'/'}>VapeShop</Link>
                </Navbar.Brand>
                <Navbar.Toggle />
            </Navbar.Header>
            <Navbar.Collapse>
                <Nav>
                    <LinkContainer to={'/'} exact>
                        <NavItem>
                            <Glyphicon glyph='home' /> Home
                            </NavItem>
                    </LinkContainer>

                    <LinkContainer to={'/fetchdata'}>
                        <NavItem>
                            <Glyphicon glyph='th-list' /> Fetch data
                            </NavItem>
                    </LinkContainer>
                </Nav>
            </Navbar.Collapse>
        </Navbar>
    );
}