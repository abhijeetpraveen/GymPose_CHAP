import { createStyles, Header, Group, Burger, Image, Container } from '@mantine/core';
import { useDisclosure } from '@mantine/hooks';

const useStyles = createStyles((theme) => ({
  header: {
    backgroundColor: theme.colors.dark[5],
    borderBottom: 0,
    marginBottom: "0px !important"
  },

  headertitle: {
    marginTop:"10px",
    fontFamily: "Anton",
    fontSize:"20px",
    color: theme.white,
  },

  inner: {
    height: 56,
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
  },

  links: {
    [theme.fn.smallerThan('sm')]: {
      display: 'none',
    },
  },

  burger: {
    [theme.fn.largerThan('sm')]: {
      display: 'none',
    },
  },

  link: {
    display: 'block',
    lineHeight: 1,
    padding: '8px 12px',
    borderRadius: theme.radius.sm,
    textDecoration: 'none',
    color: theme.white,
    fontFamily:"Anton",
    fontSize: theme.fontSizes.sm,
    fontWeight: 500,

    '&:hover': {
      backgroundColor: theme.colors.dark[4],
    },
  },

  linkLabel: {
    marginRight: 5,
  },
}));

interface HeaderSearchProps {
  links: { link: string; label: string; }[];
}

export function HeaderMenuColored({ links }: HeaderSearchProps) {
  const [opened, { toggle }] = useDisclosure(false);
  const { classes } = useStyles();

  const items = links.map((link) => {

    return (
      <a
        key={link.label}
        href={link.link}
        className={classes.link}
        onClick={() => (link.link)}
        
      >
        {link.label}
      </a>
    );
  });

  return (
    <Header height={56} className={classes.header} mb={120}>
      <Container>
        <div className={classes.inner}>
          <div style = {{display:"flex"}}>
          <Image src="https://i.imgur.com/7sAonl1.png"
            width={70} height={50}/>
          <div className = {classes.headertitle}> GYMPOSE </div>
          </div>
          <Group spacing={5} className={classes.links}>
            {items}
          </Group>
          <Burger
            opened={opened}
            onClick={toggle}
            className={classes.burger}
            size="sm"
            color="#fff"
          />
        </div>
      </Container>
    </Header>
  );
}