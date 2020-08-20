import React, { useState } from 'react';
import { Formik, Field, Form } from 'formik';
import * as Yup from 'yup';
import { Button } from '@material-ui/core'

import { Resource } from '../../../utilities/Resource';

export const NotFound = () => {
    return (
        <p>No such model form was found</p>
    );
}