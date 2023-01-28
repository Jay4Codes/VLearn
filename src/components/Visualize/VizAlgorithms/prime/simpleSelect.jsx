import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import MenuItem from "@material-ui/core/MenuItem";

const useStyles = makeStyles((theme) => ({
  selectEmpty: {
    marginTop: theme.spacing(2),
  },
}));

const SimpleSelect = (props) => {
  const classes = useStyles();
  const [age, setAge] = React.useState("0");
  const [state, setState] = React.useState({
    pos: props.pos,
  });
  const handleChange = (event) => {
    console.log("aa ", event.target.value);
    setAge(event.target.value);
    props.onAlgoChanged(state.pos, event.target.value);
  };

  return (
    <div className="ml-2 mr-2">
      <form className={classes.formControl}>
        <label id="demo-simple-select-label">Task</label>
        <select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          value={age}
          onChange={handleChange}
        >
          <MenuItem value={0} style={{ selected: true }}>
            Seive
          </MenuItem>
          <MenuItem value={1} style={{ selected: true }}>
            Archimedes Spiral
          </MenuItem>
          {/*<MenuItem value={3} style={{selected:true}} >Bitwise AND</MenuItem>*/}
          {/*<MenuItem value={4} style={{selected:true}} >Bitwise OR</MenuItem>*/}
        </select>
      </form>
    </div>
  );
};

export default SimpleSelect;
