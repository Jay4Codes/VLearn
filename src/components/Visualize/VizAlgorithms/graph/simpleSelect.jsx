import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import MenuItem from "@material-ui/core/MenuItem";
import Edge from "./edge";

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
    props.onValueChanged(state.pos, event.target.value);
  };
  // console.log(props.items);
  return (
    <div className="ml-2 mr-2">
      <form className={classes.formControl}>
        <label id="demo-simple-select-label">{props.label}</label>
        <select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          value={age}
          onChange={handleChange}
        >
          {props.items.map((item, cellidx) => {
            return (
              <MenuItem value={cellidx} style={{ selected: true }}>
                {item}
              </MenuItem>
            );
          })}
        </select>
      </form>
    </div>
  );
};

export default SimpleSelect;
