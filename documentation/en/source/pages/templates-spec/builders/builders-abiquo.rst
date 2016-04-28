.. Copyright (c) 2007-2016 UShareSoft, All rights reserved

.. _builder-abiquo:

Abiquo
======

Builder type: ``abiquo``

Require Cloud Account: Yes
`www.abiquo.com <www.abiquo.com>`_

The ``abiquo`` builder provides information for building and publishing the machine image for the Abiquo cloud platform. The Abiquo builder requires cloud account information to upload and register the machine image to the Abiquo platform.

The Abiquo builder section has the following definition:

.. code-block:: javascript

	{
	  "builders": [
	    {
	      "type": "abiquo",
	      ...the rest of the definition goes here.
	    }
	  ]
	}

Building a Machine Image
------------------------

For building an image, the valid keys are:

* ``hardwareSettings`` (mandatory): an object providing hardware settings to be used for the machine image. The following valid keys for hardware settings are:
	* ``memory`` (mandatory): an integer providing the amount of RAM to provide to an instance provisioned from the machine image (in MB).
	* ``hwType`` (optional): an integer providing the hardware type for the machine image. This is the VMware hardware type: 4 (ESXi>3.x), 7 (ESXi>4.x) or 9 (ESXi>5.x)
* ``installation`` (optional): an object providing low-level installation or first boot options. These override any installation options in the :ref:`template-stack` section. The following valid keys for installation are:
* ``diskSize`` (mandatory): an integer providing the disk size of the machine image to create. Note, this overrides any disk size information in the stack. This cannot be used if an advanced partitioning table is defined in the stack.
* ``type`` (mandatory): the builder type, ``abiquo``

Publishing a Machine Image
--------------------------

To publish an image, the valid keys are:

* ``account`` (mandatory): an object providing the abiquo cloud account information required to publish the built machine image.
* ``category`` (mandatory): a string providing the category this machine image. The category name must already be present in the abiquo platform.
* ``datacenter`` (mandatory): a string providing the datacenter name. The datacenter must already be present in the abiquo platform, and the cloud account must have access to the datacenter.
* ``description`` (mandatory): a string providing the description of what the machine image does.
* ``enterprise`` (mandatory): a string providing the enterprise resource name where to publish the machine image to. The enterprise resource must already exists in the abiquo platform, and the cloud account must have access to the enterprise resource.
* ``productName`` (mandatory): a string providing the name to be displayed for machine image. The name cannot exceed 32 characters
* ``type`` (mandatory): the builder type, ``abiquo``

Abiquo Cloud Account
--------------------

Key: ``account``

Used to authenticate the abiquo platform.

The Abiquo cloud account has the following valid keys:

* ``file`` (optional): a string providing the location of the account information. This can be a pathname (relative or absolute) or an URL.
* ``hostname`` (mandatory): a string providing the hostname or IP address where the abiquo cloud platform is running
* ``name`` (mandatory): a string providing the name of the cloud account. This name can be used in a builder section to reference the rest of the cloud account information.
* ``password`` (mandatory): a string providing the password to use to authenticate
* ``type`` (mandatory): a string providing the cloud account type: ``abiquo``.
* ``username`` (mandatory): a string providing the username to use to authenticate

.. note:: In the case where ``name`` or ``file`` is used to reference a cloud account, all the other keys are no longer required in the account definition for the builder.

Examples
--------

Basic Example
~~~~~~~~~~~~~

The following example shows an abiquo builder with all the information to build and publish a machine image to the Abiquo Cloud platform.

.. code-block:: json

	{
	  "builders": [
	    {
	      "type": "abiquo",
	      "account": {
	        "type": "abiquo",
	        "name": "My Abiquo Account",
	        "hostname": "test.abiquo.com",
	        "username": "myLogin",
	        "password": "myPassWD"
	      },
	      "hardwareSettings": {
	        "memory": 1024
	      },
	      "installation": {
	        "diskSize": 2000
	      },
	      "enterprise": "UShareSoft",
	      "datacenter": "London",
	      "productName": "CentOS Core",
	      "category": "OS",
	      "description": "CentOS Core template."
	    }
	  ]
	}

Referencing the Cloud Account
-----------------------------

To help with security, the cloud account information can be referenced by the builder section. This example is the same as the previous example but with the account information in another file. Create a json file ``abiquo-account.json``.

.. code-block:: json

	{
	  "accounts": [
	    {
	      "type": "abiquo",
	      "name": "My Abiquo Account"
	      "hostname": "test.abiquo.com",
	      "username": "myLogin",
	      "password": "myPassWD"
	    }
	  ]
	}

The builder section can either reference by using ``file`` or ``name``.

Reference by file:

.. code-block:: json

	{
	  "builders": [
	    {
	      "type": "abiquo",
	      "account": {
	        "file": "/home/joris/accounts/abiquo-account.json"
	      },
	      "hardwareSettings": {
	        "memory": 1024
	      },
	      "installation": {
	        "diskSize": 2000
	      },
	      "enterprise": "UShareSoft",
	      "datacenter": "London",
	      "productName": "CentOS Core",
	      "category": "OS",
	      "description": "CentOS Core template."
	    }
	  ]
	}

Reference by name, note the cloud account must already be created by using ``account create``.

.. code-block:: json

	{
	  "builders": [
	    {
	      "type": "abiquo",
	      "account": {
	        "name": "My Abiquo Account"
	      },
	      "hardwareSettings": {
	        "memory": 1024
	      },
	      "installation": {
	        "diskSize": 2000
	      },
	      "enterprise": "UShareSoft",
	      "datacenter": "London",
	      "productName": "CentOS Core",
	      "category": "OS",
	      "description": "CentOS Core template."
	    }
	  ]
	}