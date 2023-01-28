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

  const handleChange = (event) => {
    setAge(event.target.value);
    props.onAlgoChanged(event.target.value);
  };

  return (
    <div>
      <form className={classes.formControl}>
        <label id="demo-simple-select-label">Algorithm</label>
        <select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          value={age}
          onChange={handleChange}
        >
          {props.items.map((item, itemidx) => {
            return (
              <MenuItem key={itemidx} value={itemidx}>
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
