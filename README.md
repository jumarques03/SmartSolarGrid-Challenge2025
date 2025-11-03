# SmartSolarGrid ☀️

> Um ecossistema inteligente de gerenciamento de energia solar, integrando inversores Goodwe, a assistente virtual Alexa e uma plataforma web interativa para controle e eficiência energética em tempo real.

---

## 🧭 Sobre o Projeto

O **SmartSolarGrid** surge para aproximar o usuário de seu sistema de energia solar, que muitas vezes é complexo de monitorar. Nosso protótipo integra a assistente virtual **Alexa** e uma **plataforma web interativa**, oferecendo uma forma simples e intuitiva de acompanhar geração, consumo e armazenamento de energia.

Nosso objetivo é fornecer ao usuário mais controle sobre sua casa e trazer eficiência energética para sua rotina, respondendo ao desafio proposto pela **Goodwe** de tornar o ecossistema de energia mais inteligente, conectado e automatizado.

A solução funciona como o "cérebro" central da residência, unificando automação, inteligência e monitoramento em um único ecossistema.

---

## 🚀 Principais Funcionalidades

O SmartSolarGrid transforma dados complexos em ações simples, permitindo ao usuário:

* 🗣️ **Controle por Voz (Alexa):**
    * Consultar geração solar, nível da bateria e consumo da rede.
    * Ligar e desligar cargas prioritárias (como eletrodomésticos) com comandos de voz.
    * Solicitar dicas de economia e previsões climáticas.

* 💻 **Plataforma Web Interativa:**
    * Visualizar dados de geração e consumo em tempo real.
    * Acessar gráficos de desempenho histórico (processados a partir de dados do SEMS Goodwe).
    * Gerenciar (adicionar, editar, remover) suas cargas prioritárias.

* 🔋 **Gerenciamento Inteligente de Cargas:**
    * Acompanhar o consumo individual de cargas prioritárias.
    * Receber uma **previsão de autonomia da bateria** em tempo real, essencial para casos de falta de energia.

* 🤖 **Ajuda Inteligente (IA):**
    * Interagir com um chatbot (baseado em LLM - Gemini) treinado com métricas do sistema.
    * Receber dicas personalizadas e contextuais para otimizar o consumo e reduzir custos.

---

## 🛠️ Arquitetura e Tecnologias Utilizadas

A solução é baseada em uma arquitetura Cliente-Servidor com uma API RESTful centralizando a comunicação.

* **Backend:**
    * **Python:** Linguagem principal para a lógica de negócio e API.
    * **API RESTful:** Para comunicação entre frontend, Alexa e o servidor.
    * **Pandas:** Utilizado para análise e manipulação de dados históricos de geração e consumo.

* **Frontend:**
    * **HTML5**, **CSS3** e **JavaScript:** Para a construção da plataforma web interativa.

* **Integrações e IA:**
    * **Amazon Alexa:** Skill personalizada para processar comandos de voz.
    * **LLM (Gemini):** API externa para alimentar o chatbot inteligente.
    * **JSON:** Formato padrão para armazenamento e troca de dados entre os módulos.

---

## 🏁 Resultados

O projeto SmartSolarGrid atingiu seu objetivo principal de desmistificar o gerenciamento de energia solar e aproximar o usuário do seu sistema. Ao integrar com sucesso a assistente virtual Alexa, uma plataforma web interativa e um chatbot com IA, a solução respondeu diretamente ao desafio proposto pela Goodwe, transformando dados complexos de geração e consumo em ações práticas e acessíveis.

Mais do que uma inovação técnica, o SmartSolarGrid entrega uma experiência multimodal que promove a eficiência energética, colocando o usuário no controle real do seu consumo e demonstrando o potencial de um gerenciamento de energia mais conectado, inteligente e humano.

---
