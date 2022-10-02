import { useRef } from "react";
import { Text, Group, Button, createStyles } from "@mantine/core";
import { IconDatabase } from "@tabler/icons";
import { IconCloudUpload, IconX, IconDownload } from "@tabler/icons";

const useStyles = createStyles((theme) => ({
  wrapper: {
    position: "relative",
    marginBottom: 30,
  },

  dropzone: {
    borderWidth: 1,
    paddingBottom: 50,
    height: "40vh",
  },

  icon: {
    color:
      theme.colorScheme === "dark"
        ? theme.colors.dark[3]
        : theme.colors.gray[4],
  },

  control: {
    position: "absolute",
    width: 250,
    left: "calc(50% - 125px)",
    bottom: -20,
    backgroundColor: theme.colors.dark[9],
  },
}));

export function DropzoneButton(props:any) {
  const { classes, theme } = useStyles();
  const openRef = useRef<() => void>(null);
  
  async function uploadFile(e : any) {
    const file = e.target.files[0];
    if (file != null) {
      const data = new FormData();
      data.append("file_from_react", file);

      let response = await fetch("/url_route", {
        method: "post",
        body: data,
      });
      let res = await response.json();
      if (res.status !== 1) {
        alert("Video Uploaded");
      }
    }
    props.setUpload(true)
  }

  return (
    <>
      <input
        type="file"
        onChange={uploadFile}
        style={{ display: "none" }}
        id="contained-button-file"
      />
      <label htmlFor="contained-button-file">
        <Button size = "xl" leftIcon={<IconDatabase size={20} />} color="blue" component="span">
          Upload your Workout
        </Button>
      </label>
    </>
  );
}
