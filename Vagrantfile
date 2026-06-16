# Vagrantfile for CI/CD Docker Deployment Lab
Vagrant.configure("2") do |config|
  # Use a stable Debian base image
  config.vm.box = "debian/bookworm64"

  # VM hostname
  config.vm.hostname = "cicd-docker-vm"

  # Private network for host-only access
  config.vm.network "private_network", ip: "192.168.56.10"

  # Sync project folder into VM
  config.vm.synced_folder ".", "/home/vagrant/cicd-project"

  # VM resources
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
    vb.cpus = 2
  end

  # Provisioning: install Docker
  config.vm.provision "shell", inline: <<-SHELL
    apt-get update -y
    apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release
    curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    apt-get update -y
    apt-get install -y docker-ce docker-ce-cli containerd.io
    usermod -aG docker vagrant
  SHELL
end
