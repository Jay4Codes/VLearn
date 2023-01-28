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
    console.log(state.pos);
    setAge(event.target.value);
    props.onAlgoChanged(state.pos, event.target.value);
  };

  return (
    <div className="ml-2 mr-2">
      <form className={classes.formControl}>
        <label id="demo-simple-select-label">Algorithm</label>
        <select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          value={age}
          onChange={handleChange}
        >
          <MenuItem value={0} style={{ selected: true }}>
            Merge Sort
          </MenuItem>
          <MenuItem value={1} style={{ selected: true }}>
            Heap Sort
          </MenuItem>
          <MenuItem value={2} style={{ selected: true }}>
            Quick Sort
          </MenuItem>
        </select>
      </form>
    </div>
  );
};

export default SimpleSelect;
