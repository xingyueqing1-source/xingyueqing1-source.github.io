/*
 * The homepage content lives here. Update this file for routine maintenance;
 * the layout and interactions are kept separately in styles.css and app.js.
 * Empty optional fields or arrays are hidden automatically.
 */
window.siteContent = {
  profile: {
    name: "Yueqing Xing",
    shortName: "Yueqing",
    title: "B.Eng. Candidate in Cybersecurity",
    affiliation: "Nanjing University of Science and Technology",
    location: "Nanjing, China",
    avatar: "assets/github-avatar-circle-500.png",
    avatarAlt: "A black-and-white cat holding a newspaper mask",
    email: "xingyueqing1@gmail.com",
    cv: "output/pdf/Yueqing-Xing-CV-English.pdf",
    github: "https://github.com/xingyueqing1-source",
    scholar: "",
    interests: [
      "Machine Learning",
      "Recommender Systems",
      "Matrix Completion",
      "Uncertainty Quantification",
    ],
  },

  about: [
    "Hello — I’m Yueqing Xing, a fourth-year undergraduate in Cybersecurity at the School of Cyber Science and Engineering, Nanjing University of Science and Technology. My interests lie at the intersection of machine learning, recommender systems, matrix completion, and uncertainty quantification.",
    "I am interested in developing reliable learning methods that combine finite-sample guarantees with practical implementations. My recent work focuses on conformal inference for binary matrix completion, especially under distribution shift and model misspecification.",
  ],

  work: [
    {
      eyebrow: "Open-source research",
      title: "Conformalized 1-Bit Matrix Completion",
      shortTitle: "C1B-MC",
      authors: "Yueqing Xing",
      venue: "Accepted to an ICDM 2026 Workshop",
      description:
        "A distribution-free framework for uncertainty quantification in binary matrix completion. It uses odds-ratio weighting to address covariate shift and provides exact finite-sample marginal coverage bounds with infinity-norm truncation.",
      tags: ["Conformal prediction", "Matrix completion", "Python"],
      links: [
        {
          label: "Code",
          url: "https://github.com/xingyueqing1-source/C1B-MC",
        },
        {
          label: "Manuscript",
          url: "https://github.com/xingyueqing1-source/C1B-MC/blob/main/Conformalized%201-Bit%20Matrix%20Completion.pdf",
        },
      ],
    },
    {
      eyebrow: "Research project",
      title: "Elastic Net and Nuclear Norm Matrix Regression for Face Recognition",
      shortTitle: "ENNMR",
      authors: "Core project member",
      venue: "Accepted to ICETCI 2026",
      description:
        "A matrix-regression approach that combines Elastic Net regularization with the nuclear norm to retain two-dimensional image structure while encouraging coefficient sparsity. The project includes ADMM-based implementation, ablation studies, and convergence analysis under illumination and occlusion shifts.",
      tags: ["Face recognition", "Matrix regression", "ADMM"],
      links: [],
    },
    {
      eyebrow: "Independent project",
      title: "Feedforward Neural Network from First Principles",
      shortTitle: "NumPy FNN",
      authors: "Yueqing Xing",
      venue: "MNIST validation accuracy: 84.8%",
      description:
        "A feedforward neural network implemented with NumPy and calculus-derived gradients, without automatic differentiation. The project covers ReLU and Softmax, backpropagation, gradient descent, data preprocessing, and hyperparameter ablations.",
      tags: ["Neural networks", "NumPy", "MNIST"],
      links: [],
    },
  ],

  news: [
    {
      date: "2026.10",
      text: "The C1B-MC code and manuscript are available on GitHub.",
      url: "https://github.com/xingyueqing1-source/C1B-MC",
    },
    {
      date: "2026",
      text: "Our C1B-MC work was accepted to an ICDM 2026 Workshop.",
      url: "",
    },
    {
      date: "2026",
      text: "Our work on Elastic Net and nuclear norm matrix regression was accepted to ICETCI 2026.",
      url: "",
    },
  ],

  awards: [
    { year: "2025–2026", title: "National Scholarship" },
    { year: "2026", title: "Mathematical Contest in Modeling — Meritorious Winner" },
    {
      year: "2024",
      title: "National English Competition for College Students — National Grand Prize",
    },
    {
      year: "2024",
      title: "NECCS National Finals — First Prize in Speech and Second Prize in Debate",
    },
    {
      year: "2024",
      title: "FLTRP Vocabulary Competition — First Prize, Jiangsu Province",
    },
    {
      year: "2024",
      title: "Chinese Mathematics Competitions for College Students — Third Prize, Jiangsu Province",
    },
  ],
  services: [
    {
      date: "2025–Present",
      text: "Peer Mentor, Zhixin College, Nanjing University of Science and Technology",
    },
    {
      date: "2023–2025",
      text: "Student Assistant, Jiangyin Campus Student Affairs Office",
    },
  ],

  footer: {
    lastUpdated: "October 2026",
    note: "Designed and maintained by Yueqing Xing.",
  },
};
