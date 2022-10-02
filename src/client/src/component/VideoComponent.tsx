import React, { useState , useEffect } from "react";
import {
  Center,
  Image,
  createStyles,
  Badge,
  ActionIcon,
  Collapse,
  List,
  ThemeIcon,
  Stack,
  Group,
} from "@mantine/core";
import { IconChevronsUp } from "@tabler/icons";
import Model, { IExerciseData } from "react-body-highlighter";
import { IconCircleCheck, IconCircleX } from "@tabler/icons";
import { CardsCarousel } from "./Carousel";
import { DropzoneButton } from "./UploadBox";
import ReactPlayer from "react-player";

const useStyles = createStyles((theme) => ({
  container: {
    width: "100%",
    height: "86vh",
    backgroundColor: theme.colors.dark[6],
  },
  description: {
    borderRadius: "5px",
    display: "flex",
    height: "6vh",
  },
  text: {
    width: "97%",
    display: "flex",
  },
  exercise: {
    fontSize: "30px",
    marginLeft: "5px",
  },
  muscle: {
    color: theme.colors.dark[3],
    marginLeft: "5px",
    marginTop: "17px",
    fontSize: "15px",
  },
  diff: {
    marginLeft: "auto",
    marginTop: "auto",
    marginBottom: "auto",
  },
  icon: {
    marginLeft: "auto",
  },
  moredetails: {
    display: "flex",
  },
  model: {
    width: "37%",
  },
  stack: {
    marginLeft: "100px",

    //width: "72%",
  },
  tutorial: {
    width: "37%",
    marginTop: "10px",
    justifyContent: "center",
    textAlign: "center",
    // marginTop: "15px",
    fontSize: "30px",
  }
}));

const infoExercises = {
  BenchPress: {
    name: "Bench Press",
    muscleGroup: "Chest & Triceps",
    Pros: [
      "Increases upper body strength",
      "Improves muscular endurance",
      "Increases muscle mass",
    ],
    Cons: [
      "Risk of too much pressure on the shoulder joint",
      "High frequency/volume benching can slow muscle recovery",
      "High frequency/volume benching can stress muscles, joints, and tissues of the upper body",
    ],
    alternativeWorkouts: ["Flat dumbbell Press", "Weighted Pushups"],
    videoURL:
      "https://fitnessprogramer.com/wp-content/uploads/2021/02/Barbell-Bench-Press.gif",
  },

  Deadlift: {
    name: "Deadlift",
    muscleGroup: "Back & Legs",
    Pros: [
      "Increases strength and hypertrophy",
      "Helps with fat burning",
      "Improves grip strength",
    ],
    Cons: [
      "High risk of spinal injury",
      "Places great stress on the hips, knees, ankles and lower back",
      "Ability to lift heavy with improper form",
    ],
    alternativeWorkouts: ["Dumbbell RDLs", "Cable stiff-leg Deadlift"],
    videoURL:
      "https://fitnessprogramer.com/wp-content/uploads/2021/02/Barbell-Deadlift.gif",
  },

  Squat: {
    name: "Squat",
    muscleGroup: "Legs",
    Pros: [
      "Strengthens the knee joint",
      "Improves lower body flexibility",
      "Strengthening and hypertrophy of leg muscles (quads, calves, hamstrings)",
    ],
    Cons: [
      "Knee pain and injury",
      "Lower back injury",
      "Shoulder strain due to heavy barbell",
    ],
    alternativeWorkouts: ["Leg Press", "Hip Thursts"],
    videoURL:
      "https://fitnessprogramer.com/wp-content/uploads/2021/02/BARBELL-SQUAT.gif",
  },

  BicepCurl: {
    name: "Bicep Curl",
    muscleGroup: "Arms - Biceps",
    Pros: [
      "Strengthening and hypertrophy or arm muscles",
      "Increases bone density",
      "Easy to learn and great for beginners",
    ],
    Cons: [
      "Risk of wrist injury or strain",
      "Can cause bicep tendonitis",
      "Does not significantly improve grip strength",
    ],
    alternativeWorkouts: ["Hammer Curls", "Preacher Curls"],
    videoURL:
      "https://fitnessprogramer.com/wp-content/uploads/2022/04/Double-Arm-Dumbbell-Curl.gif",
  },

  LateralRaise: {
    name: "Lateral Raise",
    muscleGroup: "Shoulders",
    Pros: [
      "Builds rounded, muscular shoulders",
      "Improves shoulder strength, flexibility and joint stability",
      "Improves performance on compound movements",
    ],
    Cons: [
      "May experience “clicking” in your shoulders",
      "Does not target the front delts or traps",
      "Risk of shoulder injury",
    ],
    alternativeWorkouts: ["Upright Rows, Shoulder Press"],
    videoURL:
      "https://fitnessprogramer.com/wp-content/uploads/2021/02/Dumbbell-Lateral-Raise.gif",
  },

  ShoulderPress: {
    name: "Shoulders",
    muscleGroup: "Chest & Triceps",
    Pros: [
      "Engages all muscles of the shoulder",
      "Can help strengthen your triceps",
      "Can help stabilise your spine",
    ],
    Cons: [
      "Risk of shoulder injury",
      "Difficult to maintain a neutral spine",
      "May cause neck pain",
    ],
    alternativeWorkouts: ["Landmine Press", "Military Press"],
    videoURL:
      "https://fitnessprogramer.com/wp-content/uploads/2021/02/Dumbbell-Shoulder-Press.gif",
  },
};




export function VideoComponent() {
  const { classes } = useStyles();
  const [opened, setOpened] = useState(false);
  const [upload, setUpload] = useState(false);
  const [exercise,setExercise] = useState("Waiting")
  const data: IExerciseData[] = [
    { name: "Bench Press", muscles: ["chest", "triceps", "front-deltoids"] },
    { name: "Push Ups", muscles: ["chest"] },
  ];

   let count =0;

  if (upload===true && count===0){
    count = 1;
    fetch("http://localhost:5000/classify")
      .then((response) => response.json())
      .then((data) => setExercise(data["exercise"]));

  }

  
  let displayData = {
    name: "",
    muscleGroup: "",
    Pros: [''
    ],
    Cons: [''
    ],
    alternativeWorkouts: [''],
    videoURL:""
  };

  if (exercise=="Squat"){
    displayData=infoExercises.Squat
  }
  if (exercise == "ShoulderPress") {
    displayData = infoExercises.ShoulderPress;
  }
  if (exercise == "BenchPress") {
    displayData = infoExercises.BenchPress;
  }
  if (exercise=="LateralRaise"){
    displayData=infoExercises.LateralRaise
  }
  if (exercise=="BicepCurl"){
    displayData=infoExercises.BicepCurl
  }
  if (exercise == "Deadlift") {
    displayData = infoExercises.Deadlift;
  }


  return (
    <>
      <Collapse
        in={!opened}
        transitionDuration={1000}
        transitionTimingFunction="linear"
      >
        <Center className={classes.container}>
          {upload ? (
            <div
              style={{ width: 240, marginLeft: "auto", marginRight: "auto" }}
            >
              <Image
                radius="md"
                src="http://localhost:5000/video_feed"
                alt="Random unsplash image"
                style={{ width: 400, transform: "scaleY(-1)" }}
              />
            </div>
          ) : (
            <DropzoneButton setUpload={setUpload}></DropzoneButton>
          )}
        </Center>
      </Collapse>

      <div className={classes.description}>
        <div className={classes.text}>
          <div className={classes.exercise}>{displayData.name}</div>
          <div className={classes.muscle}>{displayData.muscleGroup}</div>
          {opened ? (
            <Badge
              className={classes.diff}
              color="green"
              size="lg"
              onClick={() => setOpened((o) => !o)}
            >
              {" "}
              Upload{" "}
            </Badge>
          ) : (
            <Badge
              className={classes.diff}
              color="green"
              size="lg"
              onClick={() => setOpened((o) => !o)}
            >
              {" "}
              Details Here{" "}
            </Badge>
          )}
        </div>
      </div>
      <Collapse
        in={opened}
        transitionDuration={1000}
        transitionTimingFunction="linear"
      >
        <div className={classes.tutorial}>Tutorial</div>

        <div className={classes.moredetails}>
          <Center className={classes.model}>
            <Image
              src={displayData.videoURL}
              ml="40px"
              mt="30px"
            />
          </Center>
          <Stack align="flex-start" className={classes.stack}>
            <div>
              <List
                mt={20}
                spacing="xs"
                size="lg"
                center
                icon={
                  <ThemeIcon color="teal" size={24} radius="xl">
                    <IconCircleCheck size={16} />
                  </ThemeIcon>
                }
              >
                <List.Item>{displayData.Pros[0]}</List.Item>
                <List.Item>{displayData.Pros[1]}</List.Item>
                <List.Item>{displayData.Pros[2]}</List.Item>
                <List.Item
                  icon={
                    <ThemeIcon color="red" size={24} radius="xl">
                      <IconCircleX size={16} />
                    </ThemeIcon>
                  }
                >
                  {displayData.Cons[0]}
                </List.Item>
                <List.Item
                  icon={
                    <ThemeIcon color="red" size={24} radius="xl">
                      <IconCircleX size={16} />
                    </ThemeIcon>
                  }
                >
                  {displayData.Cons[1]}
                </List.Item>
                <List.Item
                  icon={
                    <ThemeIcon color="red" size={24} radius="xl">
                      <IconCircleX size={16} />
                    </ThemeIcon>
                  }
                >
                  {displayData.Cons[2]}
                </List.Item>
              </List>
            </div>
            <Center ml={"52%"} mt={"10%"}>
              {/* <Image
                src="https://fitnessprogramer.com/wp-content/uploads/2021/02/Barbell-Bench-Press.gif"
                width={"90%"}
                height={"90%"}
                //ml={20}
              /> */}
              <CardsCarousel></CardsCarousel>
            </Center>
          </Stack>
        </div>
      </Collapse>
    </>
  );
}