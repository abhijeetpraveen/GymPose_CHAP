import React, { useState, useEffect } from "react";
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
  Paper,
  Text,
  Title,
  Button,
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
    marginTop:'30px',
    width: "40%",
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
  },
  card: {
    height: 200,
    width: 300,
    display: "flex",
    flexDirection: "column",
    justifyContent: "space-between",
    alignItems: "flex-start",
    backgroundSize: "cover",
    backgroundPosition: "center",
  },

  title: {
    fontFamily: `Anton`,
    fontWeight: 900,
    color: theme.white,
    textShadow: "-1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000",
    lineHeight: 1.2,
    fontSize: 32,
    marginTop: theme.spacing.xs,
  },

  category: {
    color: theme.black,
    opacity: 0.7,
    fontWeight: 700,
    textTransform: "uppercase",
  },
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
    alternativeWorkouts: ["Weighted Pushups", "Flat dumbbell Press"],
    videoURL:
      "https://fitnessprogramer.com/wp-content/uploads/2021/02/Barbell-Bench-Press.gif",
    images: [
      "https://i.shgcdn.com/6021fe34-c05c-4405-ad53-9fd86eb55d16/-/format/auto/-/preview/3000x3000/-/quality/lighter/",
      "https://static.strengthlevel.com/images/illustrations/dumbbell-bench-press-1000x1000.jpg",
    ],
  },

  DeadLift: {
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
    alternativeWorkouts: ["Cable stiff-leg Deadlift","Dumbbell RDL"],
    videoURL:
      "https://fitnessprogramer.com/wp-content/uploads/2021/02/Barbell-Deadlift.gif",
    images: [
      "https://www.muscleandfitness.com/wp-content/uploads/2019/09/pull-through.jpg?w=1109&quality=86&strip=all",
      "https://www.yourtrainerpaige.com/wp-content/uploads/2013/11/image59.png",
    ],
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
    images: [
      "https://www.inspireusafoundation.org/wp-content/uploads/2021/10/leg-press-machine-1024x430.png",
      "https://static.strengthlevel.com/images/illustrations/hip-thrust-1000x1000.jpg",
    ],
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
    alternativeWorkouts: ["Preacher Curls", "Hammer Curls"],
    videoURL:
      "https://fitnessprogramer.com/wp-content/uploads/2022/04/Double-Arm-Dumbbell-Curl.gif",
    images: [
      "https://www.inspireusafoundation.org/wp-content/uploads/2022/03/preacher-curl-benefits.png",
      "https://cdn.shopify.com/s/files/1/1876/4703/files/shutterstock_419477203_480x480.jpg?v=1636560233",
    ],
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
    alternativeWorkouts: ["Shoulder Press", "Upright Rows"],
    videoURL:
      "https://fitnessprogramer.com/wp-content/uploads/2021/02/Dumbbell-Lateral-Raise.gif",
    images: [
      "https://s3.amazonaws.com/prod.skimble/assets/1904357/image_iphone.jpg",
      "https://liftingfaq.com/wp-content/uploads/2022/03/upright-row-muscles-1024x770.png",
    ],
  },

  ShoulderPress: {
    name: "Shoulder Press",
    muscleGroup: "Shoulders",
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
    alternativeWorkouts: ["Military Press", "Landmine Press"],
    videoURL:
      "https://fitnessprogramer.com/wp-content/uploads/2021/02/Dumbbell-Shoulder-Press.gif",
    images: [
      "https://cdn.mos.cms.futurecdn.net/vNWR5RHgC8KsMoMGTSxEdS-1200-80.jpg",
      "https://www.fitnessandpower.com/wp-content/uploads/2016/07/landmine-anti-rotation.jpg",
    ],
  },
};

const data = [
  {
    image:
      " https://th.bing.com/th/id/OIP.yUi7hzvDDUGbv_SE8jDk2AHaEp?w=282&h=180&c=7&r=0&o=5&dpr=2&pid=1.7",
    title: "DumbbellPress",
    category: "Chest & Triceps",
  },
  {
    image:
      "https://images.unsplash.com/photo-1559494007-9f5847c49d94?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=400&q=80",
    title: "Hawaii beaches review: better than you think",
    category: "beach",
  },
  {
    image:
      "https://images.unsplash.com/photo-1608481337062-4093bf3ed404?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=400&q=80",
    title: "Mountains at night: 12 best locations to enjoy the view",
    category: "nature",
  },
];

export function VideoComponent() {
  const { classes } = useStyles();
  const [opened, setOpened] = useState(false);
  const [upload, setUpload] = useState(false);
  const [exercise, setExercise] = useState("");
  const [count, setCount] = useState(0);
  const data: IExerciseData[] = [
    { name: "Bench Press", muscles: ["chest", "triceps", "front-deltoids"] },
    { name: "Push Ups", muscles: ["chest"] },
  ];

  if (upload === true && count === 0) {
    setCount(1);
    fetch("http://localhost:5000/classify")
      .then((response) => response.json())
      .then((data) => {setExercise(data["exercise"]);setOpened((o) => !o)});
  }

  let displayData = {
    name: "",
    muscleGroup: "",
    Pros: [""],
    Cons: [""],
    alternativeWorkouts: [""],
    videoURL: "",
    images: [""],
  };


  if (exercise == "Squat") {
    displayData = infoExercises.Squat;
  }
  if (exercise == "ShoulderPress") {
    displayData = infoExercises.ShoulderPress;
  }
  if (exercise == "BenchPress") {
    displayData = infoExercises.BenchPress;
  }
  if (exercise == "LateralRaise") {
    displayData = infoExercises.LateralRaise;
  }
  if (exercise == "BicepCurl") {
    displayData = infoExercises.BicepCurl;
  }
  if (exercise == "DeadLift") {
    displayData = infoExercises.DeadLift;
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
              <Image
                radius="md"
                src="http://localhost:5000/video_feed"
                alt="Random unsplash image"
                style={{ width: 400, transform: "scaleY(-1)" }}
              />
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
              variant="filled"
              color="teal"
              size="lg"
              onClick={() => setOpened((o) => !o)}
            >
              {" "}
              Upload{" "}
            </Badge>
          ) : (
            <Badge
              className={classes.diff}
              variant="filled"
              color="teal"
              size="lg"
              onClick={() => setOpened((o) => !o)}
            >
              {" "}
              Details{" "}
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
            <Image src={displayData.videoURL} ml="40px" mt="30px" />
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
            <Center mt={"10%"}>
              <Paper
                shadow="md"
                p="xl"
                radius="md"
                sx={{ backgroundImage: `url(${displayData.images[0]})` }}
                className={classes.card}
              >
                <div>
                  <Text className={classes.category} size="xs">
                    {displayData.muscleGroup}
                  </Text>
                  <Title order={3} className={classes.title}>
                    {displayData.alternativeWorkouts[0]}
                  </Title>
                </div>
                <Button component="a" href="https://fitnessprogramer.com/exercise-primary-muscle/full-body/" variant="filled" color="dark">
                  Read Article
                </Button>
              </Paper>
              <Paper
                shadow="md"
                p="xl"
                radius="md"
                sx={{ backgroundImage: `url(${displayData.images[1]})` }}
                className={classes.card}
              >
                <div>
                  <Text className={classes.category} size="xs">
                    {displayData.muscleGroup}
                  </Text>
                  <Title order={3} className={classes.title}>
                    {displayData.alternativeWorkouts[1]}
                  </Title>
                </div>
                <Button component="a" href="https://fitnessprogramer.com/exercise-primary-muscle/full-body/" variant="filled" color="dark">
                  Read article
                </Button>
              </Paper>
            </Center>
          </Stack>
        </div>
      </Collapse>
    </>
  );
}
