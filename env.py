class StudentEnv:
  def__init__(self):
  self.progress = 0
  def reset(self):
    self.progress = 0
    return self.state()
    def state(self):
      return {"progress": self.progress)
      def step(self, action):
        if action == "study":
          self.progress += 20
        elif action == "rest":
          self.progress -= 10
          if self.progress > 100:
            self.progress = 100:
            if self.progress < 0:
              self.progress = 0
              reward = self.progress / 100
              done = self.progress == 100
              return self.state(), reward, done
