import React,{useState,useEffect} from 'react';
import { makeStyles } from '@material-ui/core/styles';
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';
import FormHelperText from '@material-ui/core/FormHelperText';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import axios from 'axios';
import { CSRF_TOKEN } from "./csrf_token";

const useStyles = makeStyles((theme) => ({
  formControl: {
    margin: theme.spacing(1),
    minWidth: 120,
  },
  selectEmpty: {
    marginTop: theme.spacing(2),
  },
}));

function Mainc() {
    const classes = useStyles();
    const [parentname,setParentName] = useState('');
  const [action, setAction] = React.useState('');
  const [ updatastate,setUpdatestate] = useState(0);
const [parent,setParent] = useState([])
  const handleChange = (event) => {
    setAction(event.target.value);
  };

  useEffect(()=>{
    axios.get(`api/parent/`).then(result=>{
    setParent(result.data)
    
    })
    .catch()
  },[updatastate])

const parentnamesubmit = ()=>{
    axios.post('api/parent/',
    {'name':parentname}, {
        headers: {
          'content-type': 'application/json',
          'X-CSRFTOKEN': CSRF_TOKEN
        }
      }).then(()=>setUpdatestate(prev=>prev+1))
}

    return (
        <div>
            <FormControl className={classes.formControl}>
        <InputLabel id="demo-simple-select-label">Catagory</InputLabel>
        <Select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          value={action}
          onChange={handleChange}
        >
          <MenuItem value={'Student'}>Student</MenuItem>
          <MenuItem value={'Teacher'}>Teacher</MenuItem>
          <MenuItem value={'Parent'}>Parent</MenuItem>
          <MenuItem value={'OfficeStaff'}>Office Staff</MenuItem>

        </Select>
      </FormControl>
      
      <form  noValidate autoComplete="off" style={{paddingTop:100,paddingBottom:10}}>
      <TextField id="standard-basic" label="Add parent name" onChange={(e)=>setParentName(e.target.value)}/>
      <Button variant="contained" color="primary" size='small' onClick={()=>parentnamesubmit()}>
        Add
      </Button>
    </form>
    <Typography variant="h6" component="h6" gutterBottom>
       List of parents
      </Typography>
      
      <ul>
          {parent.map(item=> <li key={item.id}>{item.name}</li>)}
         
      </ul>
        </div>
    )
}

export default Mainc
